import os
from nltk.tag.stanford import StanfordPOSTagger
java_path = "/home/sree/bigdata/jdk1.8.0_181/bin/java"
os.environ['JAVAHOME'] = java_path



__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"




path_to_model = "models/english-bidirectional-distsim.tagger"
path_to_jar = "models/stanford-postagger.jar"
tagger = StanfordPOSTagger(path_to_model, path_to_jar)
tagger.java_options='-mx4096m'
sentence = 'This is testing'
print(tagger.tag(sentence.split()))






raw_data_path = "/home/sree/data/scisci/nature_science_journal_data.pql"
data = pd.read_pickle(raw_data_path)
data = data[data.Journal == "NATURE"]
