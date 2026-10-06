;functions

(require 2htdp/image)

(define (bulb c)
  (circle 10 "solid" c))

(define (rec w h c)
  (rectangle w h "solid" c))

(overlay (above (bulb "red")
                (bulb "yellow")
                (bulb "green")
                )

         (rectangle 30 70 "solid" "black")
         (rec 40 80 "green"))

(define (area h w)
  (* h w))

(area 10 2)

; rectangle area
(define (rectangle-area h w)
  (* h w))

(rectangle-area 10 2)

;greeting
(define (greet name)
  (string-append "Hello " name "!"))
(greet "nana")

; logo
(define (logo sign)
  (text sign 30 "red"))

(logo "cybernerddd")

;badge maker
(define (make-badge f-name alias)
  (overlay
   (above (text f-name 15 "blue")
          (text alias 10 "blue"))
   (rectangle 120 80 "solid" "grey")))

(make-badge "Emmanuel" "cybernerddd")

;celsius-to-fahrenheit
(define (celsius-to-fahrenheit celsius)
  (+ (* celsius 1.8) 32))

(celsius-to-fahrenheit 25)

;testing function in fnction
(define (cyber-badge name)
  (overlay (above (logo name)
                  (text "cybernerddd" 12 "red"))
           (square 100 "outline" "blue")))

(cyber-badge "MAX")
