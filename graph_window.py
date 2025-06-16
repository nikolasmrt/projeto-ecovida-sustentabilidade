from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainter, QPixmap, QImage


try:
    from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
    QTCHARTS_AVAILABLE = True
except ImportError:
    QTCHARTS_AVAILABLE = False
    print("Aviso: PySide6-Charts não encontrado em graph_window.py. Gráficos interativos desativados.")


if not QTCHARTS_AVAILABLE:
    import matplotlib.pyplot as plt
    from io import BytesIO


from connection import obter_dados_grafico_por_categoria

class GraphWindow(QDialog):
    def __init__(self, usuario_id, parent=None):
        super().__init__(parent)
        self.usuario_id = usuario_id
        self.setWindowTitle("Gráfico de Consumo por Categoria")
        self.setFixedSize(800, 600) 
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) 

        self.setup_ui()
        self.apply_qss()
        self.load_graph()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        title_label = QLabel("Consumo de Hábitos por Categoria")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        if QTCHARTS_AVAILABLE:
            self.chart_view = QChartView()
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
            self.chart_view.chart().setTitle("Dados de Consumo (Interativo)")
            self.chart_view.chart().setAnimationOptions(QChart.SeriesAnimations)
            main_layout.addWidget(self.chart_view)
        else:
            self.image_label = QLabel() 
            self.image_label.setAlignment(Qt.AlignCenter)
            main_layout.addWidget(self.image_label)
            fallback_message = QLabel("PySide6-Charts não disponível. Exibindo gráfico estático.")
            fallback_message.setAlignment(Qt.AlignCenter)
            fallback_message.setStyleSheet("color: orange; font-style: italic;")
            main_layout.addWidget(fallback_message)


        close_button = QPushButton("Fechar")
        close_button.clicked.connect(self.accept) 
        close_button.setFixedSize(120, 40)
        main_layout.addWidget(close_button, alignment=Qt.AlignCenter)

    def apply_qss(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #3e5c76; /* Cor de fundo para a janela do gráfico */
                color: #ecf0f1;
                font-family: 'Segoe UI', 'Arial';
            }
            QLabel {
                color: #ecf0f1;
            }
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

    def load_graph(self):
        dados = obter_dados_grafico_por_categoria(self.usuario_id)

        if not dados:
            if QTCHARTS_AVAILABLE:
                self.chart_view.chart().setTitle("Consumo por Categoria (Sem Dados)")
            else:
                self.image_label.setText("Nenhum dado para exibir no gráfico.")
            QMessageBox.information(self, "Dados Ausentes", "Nenhum dado de hábito encontrado para gerar o gráfico.")
            return

        categorias = [dado[0] for dado in dados]
        quantidades = [float(dado[1]) for dado in dados]

        if QTCHARTS_AVAILABLE:
           
            self.chart_view.chart().removeAllSeries()
            for axis in self.chart_view.chart().axes():
                self.chart_view.chart().removeAxis(axis)

            set0 = QBarSet("Consumo Total")
            for q in quantidades:
                set0.append(q)

            series = QBarSeries()
            series.append(set0)
            self.chart_view.chart().addSeries(series)

            axisX = QBarCategoryAxis()
            axisX.append(categorias)
            self.chart_view.chart().addAxis(axisX, Qt.AlignBottom)
            series.attachAxis(axisX)

            axisY = QValueAxis()
            axisY.setLabelFormat("%.1f")
            axisY.setTitleText("Quantidade Total")
            self.chart_view.chart().addAxis(axisY, Qt.AlignLeft)
            series.attachAxis(axisY)

            self.chart_view.chart().setTitle("Consumo por Categoria")
            self.chart_view.chart().legend().setVisible(False)
        else:
            
            plt.figure(figsize=(7, 5)) 
            plt.bar(categorias, quantidades, color='mediumseagreen')
            plt.xlabel("Categoria")
            plt.ylabel("Quantidade Total")
            plt.title("Consumo por Categoria")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            
            buffer = BytesIO()
            plt.savefig(buffer, format='png', transparent=True, bbox_inches='tight') 
            plt.close() 
            buffer.seek(0)
            
            image = QImage.fromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(image)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.setScaledContents(True) 