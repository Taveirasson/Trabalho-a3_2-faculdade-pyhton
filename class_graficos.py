from io import BytesIO
import base64
import plotly.express as px
import plotly.graph_objects as go

class Graficos:
    def __init__(self, df):
        """
        Inicializa a classe com um DataFrame.
        """
        self.df = df

    def _salvar_grafico(self, fig):
        """
        Salva o gráfico em um formato de imagem base64.
        """
        img_buffer = BytesIO()
        fig.write_image(img_buffer, format='png')
        img_buffer.seek(0)
        img_str = base64.b64encode(img_buffer.read()).decode('utf-8')
        return img_str
 

    def gerar_grafico(self, tipo_grafico, dado1, dado2):
        """
        Gera um gráfico com base no tipo e nos dados fornecidos.
        """
        graficos_disponiveis = {
            'barras': self.gerar_grafico_barra,
            'pizza': self.gerar_grafico_pizza, #1
            'dispersao': self.gerar_grafico_dispersao,
            'linha': self.gerar_grafico_linha,
            'area': self.gerar_grafico_area,
            'area_empilhada': self.gerar_grafico_area_empilhada,
            'barras_empilhadas': self.gerar_grafico_barras_empilhadas
            # Adicione outras entradas conforme necessário
        }

        if dado1 is None and dado2 is None:
            return 'Nenhum dado selecionado'

        if tipo_grafico in graficos_disponiveis:
            graph = graficos_disponiveis[tipo_grafico](dado1, dado2)
        else:
            graph = None

        return graph 

    def gerar_grafico_barra(self, x=None, y=None):
        """
        Gera um gráfico de barras.
        """

        if x is not None and y is not None:
           title = f'Gráfico de Barras - {y} por {x}'
           labels = {x: x, y:y}
        elif x is not None and y is None:
            title = f'Gráfico de Barras - Contagem por {x}'
            labels = {x: x, 'count': 'Contagem'}
        else:
            title = f'Gráfico de Barras - {y} por Contagem'
            labels = {'count': 'Contagem',y:y}

        fig = px.bar(self.df, x=x, y=y, title=title, labels=labels)
        return self._salvar_grafico(fig)

    def gerar_grafico_pizza(self, dado, lixo):
        """
        Gera um gráfico de pizza.
        """
        fig = px.pie(self.df, names=dado, title=f'Gráfico de Pizza - Distribuição por {dado}')

        fig.update_traces(textinfo='percent+label', pull=[0.05] * len(self.df[dado]),
                          showlegend=False, selector=dict(type='pie'))

        return self._salvar_grafico(fig)
    
    def gerar_grafico_dispersao(self, x=None, y=None):
        """
        Gera um gráfico de dispersão.
        """

        if x is not None and y is not None:
           title = f'Gráfico de Dispersão - {y} em função de {x}'
           labels = {x: x, y:y}
        elif x is not None and y is None:
            title = f'Gráfico de Dispersão - Contagem por {x}'
            labels = {x: x, 'count': 'Contagem'}
        else:
            title = f'Gráfico de Dispersão - {y} por Contagem'
            labels = {'count': 'Contagem',y:y}

        fig = px.scatter(self.df, x=x, y=y, title=title, labels=labels)
        return self._salvar_grafico(fig)

    def gerar_grafico_linha(self, x=None, y=None):
        """
        Gera um gráfico de linha.
        """

        if x is not None and y is not None:
           title = f'Gráfico de Linha - {y} em função de {x}'
           labels = {x: x, y:y}
        elif x is not None and y is None:
            title = f'Gráfico de Linha - Contagem por {x}'
            labels = {x: x, 'count': 'Contagem'}
        else:
            title = f'Gráfico de Linha - {y} por Contagem'
            labels = {'count': 'Contagem',y:y}

        #title = f'Gráfico de Linha - {y} em função de {x}' if y else f'Gráfico de Linha - {x} por contagem'
        #labels = {'count': 'Contagem', x: x} if not y else {x: x, y: y}

        fig = px.line(self.df, x=x, y=y, title=title, labels=labels)
        return self._salvar_grafico(fig)
    
    def gerar_grafico_area(self, x = None, y=None):
        """
        Gera um gráfico de área.
        """

        if x is not None and y is not None:
           title = f'Gráfico de Área - {y} em função de {x}'
           labels = {x: x, y:y}
        elif x is not None and y is None:
            title = f'Gráfico de Área - Contagem por {x}'
            labels = {x: x, 'count': 'Contagem'}
        else:
            title = f'Gráfico de Área - {y} por Contagem'
            labels = {'count': 'Contagem',y:y}

        #title = f'Gráfico de Área - {y} por {x}' if y else f'Gráfico de Área - {x} por contagem'
        #labels = {'count': 'Contagem', x: x} if not y else {x: x, y: y}

        fig = px.area(self.df, x=x, y=y, title=title, labels=labels)
        return self._salvar_grafico(fig)
    
    def gerar_grafico_area_empilhada(self, x=None, y=None):
        """
        Gera um gráfico de área empilhada.
        """
        
        if x is not None and y is not None:
           title = f'Gráfico de Área Empilhada - {y} em função de {x}'
           labels = {x: x, y:y}
        elif x is not None and y is None:
            title = f'Gráfico de Área Empilhada - Contagem por {x}'
            labels = {x: x, 'count': 'Contagem'}
        else:
            title = f'Gráfico de Área Empilhada - {y} por Contagem'
            labels = {'count': 'Contagem',y:y}

        #title = f'Gráfico de Área Empilhada - {x} por {y}'
        #labels = {'count': 'Contagem', x: x}

        fig = px.area(self.df, x=x, title=title, labels=labels, color=y)
        return self._salvar_grafico(fig)
    
    def gerar_grafico_barras_empilhadas(self, x=None, y=None):
        """
        Gera um gráfico de barras empilhadas.
        """

        if x is not None and y is not None:
           title = f'Gráfico de Barras Empilhadas - {y} em função de {x}'
           labels = {x: x, y:y}
        elif x is not None and y is None:
            title = f'Gráfico de Barras Empilhadas - Contagem por {x}'
            labels = {x: x, 'count': 'Contagem'}
        else:
            title = f'Gráfico de Barras Empilhadas - {y} por Contagem'
            labels = {'count': 'Contagem',y:y}

        
        #title = f'Gráfico de Barras Empilhadas - {x} por {y}'
        #labels = {x: x, 'count': 'Contagem'}

        fig = px.bar(self.df, x=x, title=title, labels=labels, color=y)
        return self._salvar_grafico(fig)