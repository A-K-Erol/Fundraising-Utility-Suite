
<p align="center">
  <img src="https://github.com/A-K-Erol/Fundraising-Utility-Suite/assets/43559753/3928bee8-c494-41d4-899c-1efa0c9a9a5f" style="width: 30%;" />
</p>
Hi! This is a project that I created inspired by a couple of the nonprofits I consult for. Zeke Jackson, Executive Director of People for PSEO, was always interested in getting chatGPT to write grant applications, but didn't like that it didn't have the context necessary to do so. Ukraine Mental Help was struggling also with grant-writing and marketing in English due to language barriers.

The core functionality of this application is two-fold:

First is a text-generation tool for grant-writing, social-media marketing, and email-marketing. The model accepts inputs in the form of a prompt and various parameters such as purpose, length, and key values. Then, it is passed into a trained LangChain vector store, which runs on the ADA model. Token limits are overcome by iteratively passing the prompt in until a stop token is reached. The output from the vector store is used as input into a fine-tuned GPT-4 model based on my grant-writing style, though in the version uploaded into the repository, I believe I just use standard GPT-3 for cost-savings.

Second is an Apollo based lead-generation tool. There isn't much to look at here; I utilize the API to search for suitable profiles, and then use GPT to make them into a pretty presentable report. It might be worth experimenting in the future with having chatgpt generate React components directly.

For the development details:

Back-end: Standard Flask REST-API that interacts directly with the trained AI models based on http requests. Tested it with Postman client.

Front-end: React Web Application, created with ViteJS. Axios used for REST interactions. BootstrapCSS used for styling.

And here's an example of what it looks like:
<p align="center">
  <img width="752" alt="image" src="https://github.com/A-K-Erol/Fundraising-Utility-Suite/assets/43559753/da9ca63e-a0ad-43e0-b9dd-b1109eed7ad9">
</p>
