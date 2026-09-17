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


(substring "Crocodile" 0 4)
(substring "Crocodile" 5)
(string-length "Cybersecurity")
(string-length "Cybernerddd")
(string-length "Ethical hacker")
(string-append "I" " " "am" " " "learning" " " "Racket.")

(above (circle 10 "solid" "red")
       (circle 10 "solid" "yellow")
       (circle 10 "solid" "green"))


(overlay (text "WARNING" 30 "white")
         (regular-polygon 66 8 "solid" "red"))


(overlay 
         (beside (text "HACK" 30 "black")
                 (circle 10 "solid" "blue"))
         (rectangle 200 60 "solid" "green"))

(overlay (rectangle 150 90 "outline" "black")
 (above (text "CYBER" 20 "black")
        (beside (circle 10 "solid" "blue")
        (circle 10 "solid" "green")
        (circle 10 "solid" "red"))
        (text "NERDDD" 20 "black")))
        
