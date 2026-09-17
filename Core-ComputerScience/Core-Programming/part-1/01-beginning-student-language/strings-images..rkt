;rocket
;; strings and images
(require 2htdp/image)

"Emmanuel"
"Ampah"

(string-append "Emmanuel" " " "Ampah")

(string-length "Maxwell")

(substring "Crocodile" 2 4)

(substring "Caribou" 2)

; images

(beside (circle 10 "outline" "blue")
        (rectangle 60 40 "solid" "red")
        (text "hello" 20 "green"))

(overlay (circle 10  "solid" "red")
         (circle 20  "solid" "blue")
         (circle 30  "solid" "green"))
       
(overlay (text "STOP" 48 "white")
         (regular-polygon 60 8 "solid" "red"))
