
;; image-area-starter.rkt

(require 2htdp/image)

; 
; PROBLEM:
; 
; DESIGN a function called image-area that consumes an image and produces the 
; area of that image. For the area it is sufficient to just multiple the image's 
; width by its height.  Follow the HtDF recipe and leave behind commented 
; out versions of the stub and template.
; 


;; Image -> Natural
;; produces the area of the image given

(check-expect (image-area (rectangle 3 4 "solid" "red")) 12)
(check-expect (image-area (rectangle 5 4 "solid" "blue")) 20)

;(define (image-area img) 0)   ;stub

;(define (image-area img)    ;template
 ; (... img))

(define (image-area img)
  (* (image-height img) (image-width img)))
