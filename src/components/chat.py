from reactpy import component, html
from ..utils.css_loader import load_css
from ..hooks.use_chat import use_chat

@component
def ChatMessage(message):
    return html.div(
        {
            "class": f"chat-message {message['sender'].lower()}-message"
        },
        html.div(
            {"class": "message-content"},
            html.strong(message["sender"]),
            html.span({"class": "timestamp"}, message["timestamp"]),
            html.p(message["text"]),
        )
    )

@component
def Chat():
    messages, new_message, set_new_message, send_message = use_chat()

    return html.div(
        {"class": "chat-container"},
        load_css('chat.css'),
        html.h2("Chat"),
        html.div(
            {"class": "messages-container"},
            [ChatMessage(msg) for msg in messages]
        ),
        html.form(
            {
                "class": "chat-form",
                "on_submit": send_message
            },
            html.input({
                "type": "text",
                "value": new_message,
                "on_change": lambda e: set_new_message(e["target"]["value"]),
                "placeholder": "Type your message...",
            }),
            html.button({"type": "submit"}, "Send"),
        )
    )
