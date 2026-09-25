;racket

(require 2htdp/image)

(define age 2)
(define mass 4)
(= age mass); for numbers

;comparing strings
(string=? "foo" "bar") ; returns false

(define w1 (rectangle 10 20 "solid" "red"))
(define w2 (rectangle 20 10 "solid" "blue"))

; image comparisons
(< (image-width w1)
   (image-width w2))

