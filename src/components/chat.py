from reactpy import component, html, hooks
from ..utils.css_loader import load_css

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
def Chat(messages, on_new_message):
    new_message, set_new_message = hooks.use_state("")

    def handle_submit(event):
        event.preventDefault()
        if new_message.strip():
            on_new_message(new_message)
            set_new_message("")

    return html.div(
        {"class": "chat-container"},
        load_css('chat.css'),
        html.h2("Chat"),
        html.div(
            {"class": "messages-container"},
            [
                html.div(
                    {"key": f"message-{msg['id']}"}, 
                    ChatMessage(msg)
                ) for msg in messages
            ]
        ),
        html.form(
            {
                "class": "chat-form",
                "on_submit": handle_submit
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
