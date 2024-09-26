from winotify import Notification, audio

toast = Notification(app_id="Rock, Paper or Scissors",
                     icon= r"C:\Users\artho\OneDrive\Desktop\Python\Personal\ii.png",
                     title="RESULT",
                     msg="YOU WON THE GAME!!!",
                     )

toast.set_audio(audio.Default, loop= False)

toast.add_actions(label= "Clique aqui!", launch= "https://www.instagram.com/?hl=pt-br")

toast.show() 