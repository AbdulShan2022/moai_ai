
css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.st-emotion-cache-janbn0 {
   background-color: #2b313e;
}

/* AI Chat Message */
    
.st-emotion-cache-4oy321 {
    background-color: #475063;
}

section[data-testid="stSidebar"] {
    width: 380px !important;
}
.st-emotion-cache-12skds7 {
    padding: 0px !important;
}
.st-emotion-cache-1mi2ry5{
padding: 1rem 1rem 0.5rem 1rem !important;
}
.st-emotion-cache-1itdyc2{
    .st-emotion-cache-5drf04{
    height: 5rem !important;
    width: 13rem !important;
    }
}
.st-emotion-cache-1wntj30{
background-color: #475063 !important;
}
.st-emotion-cache-1sno8jx{
>h2 {
padding: 0.5rem 0 !important;
}
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''