;; tall-starter.rkt

(require 2htdp/image)
; 
; PROBLEM:
; 
; DESIGN a function that consumes an image and determines whether the 
; image is tall.
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


;; Image -> Boolean
;; produce true when the image is tall(image-height is graeater than image-width)

(check-expect (tall? (rectangle 3 2 "solid" "red")) false)
(check-expect (tall? (rectangle 2 3 "solid" "red")) true)
(check-expect (tall? (rectangle 3 3 "solid" "red")) false)

; (define (tall? img) false)   ;stub

;(define (tall? img)           ;template
 ; (... img))

(define (tall? img)
  (> (image-height img) (image-width img)))
