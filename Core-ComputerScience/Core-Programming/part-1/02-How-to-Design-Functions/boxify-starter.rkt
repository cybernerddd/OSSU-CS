(require 2htdp/image)

;; boxify-starter.rkt

; 
; PROBLEM:
; 
; Use the How to Design Functions (HtDF) recipe to design a function that consumes an image, 
; and appears to put a box around it. Note that you can do this by creating an "outline" 
; rectangle that is bigger than the image, and then using overlay to put it on top of the image. 
; For example:
; 
; (boxify (ellipse 60 30 "solid" "red")) should produce .
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 



;; Image -> Image
;; Produce a rectangle overlay on the image given, with 2 pixels wider and taller than the given image

(check-expect (boxify (ellipse 60 30 "solid" "red")) (overlay (rectangle 62 32 "outline" "black")
                                                              (ellipse 60 30 "solid" "red")))
(check-expect (boxify (ellipse 90 30 "solid" "red")) (overlay (rectangle 92 32 "outline" "black")
                                                              (ellipse 90 30 "solid" "red")))
(check-expect (boxify (star 40 "solid" "blue")) 
              (overlay (rectangle (+ (image-width (star 40 "solid" "blue")) 2) 
                                  (+ (image-height (star 40 "solid" "blue")) 2) 
                                  "outline" "black")
                       (star 40 "solid" "blue")))

;(define (boxify img) (rectangle 20 30 "outline" "black"))    ;stub

;(define (boxify img)                                         ;template
; (... img))

(define (boxify img)
  (overlay (rectangle (+ (image-width img) 2) (+ (image-height img) 2) "outline" "black")
           img))
