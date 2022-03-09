import src.helpers.cli_prompts as cp

import json
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

class BertopicTraining():
    def __init__(self, docs, out_dir, out_file):
        self.dumps = json.dumps({})

        self.content = []

        print(self.dumps)

        # Grab only content from scrapy .json file
        for x in self.dumps:
            self.content.append(self.dumps["content"])

        self.output_directory = out_dir
        self.output_filename = out_file

    def trainModel(self):
        topic_model = BERTopic()
        topics = None
        probs = None

        try:
            topics, probs = topic_model.fit_transform(self.dumps)
        except RuntimeError as e:
            cp.print_insufficient_resources()

        vectorizer_model = CountVectorizer(stop_words="english", ngram_range=(1, 5))
        topic_model.update_topics(self.dumps, topics, vectorizer_model=vectorizer_model)
    
        self.writeTrainingDataToDisk(topic_model,
                                     topic_model.get_topic_info(), 
                                     topic_model.get_topics(),
                                     topic_model.get_representative_docs(), 
                                     topic_model.get_topic_freq())

        self.writeVisualizationFilesToDisk(topic_model)

        print(topic_model.get_topic_info())

    def writeTrainingDataToDisk(self, topicModel, topicInfo, allTopicInfo, repDoc, topicFrequency):
        topicInfoDir = os.path.join(self.outputDir, self.outputFilename + "_TOPIC_INFO" + ".txt")
        allTopicInfoDir = os.path.join(self.outputDir, self.outputFilename + "_ALL_TOPIC_INFO" + ".txt")
        repDocDir = os.path.join(self.outputDir, self.outputFilename + "_REPERSENTITIVE_DOCS" + ".txt")
        topicFrequencyDir = os.path.join(self.outputDir, self.outputFilename + "_TOPIC_FREQUENCY" + ".txt")
        topicModelDir = os.path.join(self.outputDir, self.outputFilename + "_TOPIC_MODEL" + ".bin")

        TIF = open(topicInfoDir, "w")
        TIF.write(topicInfo.to_string())
        TIF.close()

        AIF = open(allTopicInfoDir, "w")
        AIF.write(str(allTopicInfo))
        AIF.close()

        RDF = open(repDocDir, "w")
        print(repDoc, file=RDF)
        RDF.close()

        TFF = open(topicFrequencyDir, "w")
        TFF.write(topicFrequency.to_string())
        TFF.close()

        topicModel.save(topicModelDir)

    def writeVisualizationFilesToDisk(self, topicModel):
        path = self.outputDir + "/visualizations/"

        try:
            os.mkdir(path)
        except FileExistsError:
            print("Visualizations folder already exists, writing to previously created folder.")

        vt = topicModel.visualize_topics()
        vt.write_html(path + "topics_visual.html")

        vhi = topicModel.visualize_hierarchy()
        vhi.write_html(path + "hierarchy_visual.html")

        vb = topicModel.visualize_barchart()
        vb.write_html(path + "barchart_visual.html")

        vhe = topicModel.visualize_heatmap()
        vhe.write_html(path + "heatmap_visual.html")

