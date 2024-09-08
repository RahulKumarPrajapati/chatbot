from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
import time

class LLMTask():
    """
    Celery Task class to support loading LLM model.
    """

    __conversation = None
    __llm = None
    __models = {
        'mistral-Q5_K_M' : 'mistral-7b-instruct-v0.2.Q5_K_M.gguf',
        'mistral-Q4_K_M' : 'mistral-7b-instruct-v0.2.Q4_K_M.gguf'
    }
    __callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    __n_gpu_layers = -1  # The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
    __n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    __template = """
    [INST] The following is the conversation between Human and Chatbot. Chatbot is talkative and provides the best possible answers. If Chatbot doesn't know the answer, it simply says "I don't know."
    Human: {input} [/INST]
    Chatbot:
    """
    __prompt = PromptTemplate(template=__template, input_variables=["input"])
    
    def __init__(self) -> None:
        super().__init__()
        pass

    @classmethod
    def modelLoad(cls):
        """
        Load model on first call (i.e first task processed)
        """
        if not LLMTask.__llm and not LLMTask.__conversation:
            LLMTask.__llm = LlamaCpp(
                model_path= 'models\\mistral\\' + LLMTask.__models['mistral-Q4_K_M'],
                max_tokens=1500,  # Output tokens that will be generated
                n_gpu_layers = LLMTask.__n_gpu_layers,
                n_batch = LLMTask.__n_batch,
                n_ctx=2000,       # Maximum context window length
                stop=["Human:"],
                echo=False,       # Echo the prompt in the output
                top_k=1,
                callback_manager=LLMTask.__callback_manager,
                verbose=True,     # Verbose is required to pass to the callback manager
            )
            LLMTask.__conversation = LLMChain(llm = LLMTask.__llm, prompt = LLMTask.__prompt, verbose = True)

    def getHint(self, problem_statement):
        try:
            t = time.time()
            if problem_statement:
                res = LLMTask.__conversation.invoke(problem_statement)
            print('Total time taken: {0} seconds: ' , time.time() - t)
            return {'answer': res['text'].split('\n')}
        except Exception as e:
            print(f'chatService --> getHint --> Error: {e}')