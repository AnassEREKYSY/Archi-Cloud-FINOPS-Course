const { TextAnalyticsClient, AzureKeyCredential } = require('@azure/ai-text-analytics');

const endpoint = "https://AIServiceLab8.cognitiveservices.azure.com/";
const apiKey = "10bbddf9ca524ef9b5c9b2be64972a81";

const textAnalyticsClient = new TextAnalyticsClient(endpoint, new AzureKeyCredential(apiKey));

async function analyzeText() {
    const documents = [
        "I had the best day of my life. This is so good!",
        "I am so sad and unhappy with my current situation."
    ];

    const sentimentResult = await textAnalyticsClient.analyzeSentiment(documents);
    sentimentResult.forEach((result, index) => {
        console.log(`Document ${index + 1} sentiment: ${result.sentiment}`);
    });

    const keyPhrasesResult = await textAnalyticsClient.extractKeyPhrases(documents);
    keyPhrasesResult.forEach((result, index) => {
        console.log(`Document ${index + 1} key phrases: ${result.keyPhrases.join(', ')}`);
    });
}

analyzeText().catch(err => {
    console.error("The following error occurred:", err);
});
