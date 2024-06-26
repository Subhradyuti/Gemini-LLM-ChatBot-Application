# Gemini LLM Application

This is a Streamlit-based web application that leverages Google's Generative AI (Gemini Pro model) to provide responses to user queries. The application allows users to input questions and receive responses in real-time, while maintaining a chat history.

## Features

- **Real-time Q&A**: Input questions and get responses from the Gemini Pro model.
- **Chat History**: Maintains a history of the conversation.
- **Clear Chat**: Option to clear the chat history.
- **Error Handling**: Proper error handling for API responses.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/gemini-llm-app.git
    cd gemini-llm-app
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your Google API key to the `.env` file:
      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

## Usage

1. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501` to access the application.

3. **Input a question** in the text box and click the "Ask the question" button to get a response.

4. **Clear the chat history** using the "Clear Chat" button if needed.

## Example

Here is an example of how the chat history might look:
![image](https://github.com/Subhradyuti/Gemini-LLM-ChatBot-Application/assets/133640355/3cdd861d-17f4-4f61-beda-2fe6582e007c)

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](MIT) file for details.

