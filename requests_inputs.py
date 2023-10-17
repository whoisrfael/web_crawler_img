import requests
from bs4 import BeautifulSoup

def get_web_content(url: str) -> requests.Response:
    """
    Make a GET request to the provided URL and return the response.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    return requests.get(url, headers=headers)

def extract_paragraphs(content: bytes) -> list:
    """
    Extract and return all paragraphs from the provided HTML content.
    """
    soup = BeautifulSoup(content, 'html.parser')
    return [p.text for p in soup.find_all('p')]

def format_url(url: str) -> str:
    """
    Format the provided URL to ensure it starts with a scheme (http/https).
    """
    if not url.startswith(('http://', 'https://')):
        return 'https://' + url
    return url

def main():
    # Solicitando ao usuário para inserir a URL
    url = input("Por favor, insira a URL para extrair parágrafos: ")
    url = format_url(url)  # Format the URL to ensure it's valid

    try:
        response = get_web_content(url)
        
        if response.status_code == 200:
            paragraphs = extract_paragraphs(response.content)
            for p in paragraphs:
                print(p)
        else:
            print(f"Erro ao acessar o site. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")

if __name__ == '__main__':
    main()
