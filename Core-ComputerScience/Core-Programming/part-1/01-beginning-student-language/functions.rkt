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
