# Conexão com o Sharepoint
from shareplum import Site, Office365
from shareplum.site import Version

# Variáveis
sharepoint_user = 'usuario@sharepoint.com'
sharepoint_password = 'senha' # Colocar a senha da conta
sharepoint_url_base = 'https://exemplooffice.sharepoint.com/sites/pasta_do_projeto'
pasta_no_sharepoint = '%2Fsites%2Fpasta_do_projeto%2FDocumentos%20Compartilhados%2FAcompanhamento'

# Função para fazer a autenticação no sharepoint
def login_sharepoint(sharepoint_password, sharepoint_user, sharepoint_url_base):
    try:
        authcookie = Office365('https://acocearenseoffice.sharepoint.com', username=sharepoint_user, password=sharepoint_password).GetCookies()
        site = Site(sharepoint_url_base, version=Version.v365, authcookie=authcookie)
        print('Autenticação OK!')
        return site 

    except Exception as e:
        print(f'Falha na autenticação...\n{str(e)}')
        return ""

# Função para fazer o upload dos dados para o sharepoint
def envia_sharepoint(pasta_no_sharepoint, site : any, caminho_arquivo, nome_tabela : str):
    try:
        print(f'Subindo tabela: {nome_tabela} para o sharepoint')
        # Definindo pasta de destino
        folder = site.Folder(pasta_no_sharepoint)

        # Subindo dados para o sharepoint
        folder.upload_file(caminho_arquivo, nome_tabela)

    except Exception as e:
        print(f'Falha ao enviar o arquivo: {nome_tabela}')
        print(str(e))

#### EXEMPLO DE USO

# Salvando dados no sharepoint
site = login_sharepoint(sharepoint_password, sharepoint_user, sharepoint_url_base)

if type(site) != str:
    envia_sharepoint(pasta_no_sharepoint, site, r"C:\Users\Gbrlm\Downloads\teste.png", 'teste.png')