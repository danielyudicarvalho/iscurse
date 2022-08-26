from iscurse import Analyzer

analyzer = Analyzer()


analyzer.analyse('esse é um filme muito ruim')
print(analyzer.get_score())
print(analyzer.get_sentiment())
print(analyzer.get_binary())
print(analyzer.get_emoji())