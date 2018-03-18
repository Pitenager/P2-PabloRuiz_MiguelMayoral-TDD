import sys
from sample.text_analyzer import TextAnalyzer

if __name__ == "__main__":
    args = sys.argv[1:]
    print("Welcome to the awesome text analyzer !\nThe results are:")

    #En caso de que se quiera ejecutar desde IDE, descomentar la siguiente línea y comentar la consecutiva
    #TextAnalyzer.run('http://websitetips.com/articles/copy/lorem/ipsum.txt')
    TextAnalyzer.run(args[0])
