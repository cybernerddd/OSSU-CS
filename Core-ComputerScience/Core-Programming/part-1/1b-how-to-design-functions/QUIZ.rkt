; PROBLEM:
; 
; Design a function that consumes two images and produces true if the first is larger than the second.
; 
; Note that limitations of the edX assessment tool mean that you cannot use images directly in your .rkt file.
; You can of course use image primitives like rectangle. But you cannot paste actual images into your .rkt
; file for this quiz, even though you normally can do that in BSL.
; Furthermore, unfortunately the assessment tool does not preserve the indentation of your code.
; When it comes time for the self-assessment, you can assess your original .rkt file, or copy
; your submission back into DrRacket and press cmd/ctr-I.


(require 2htdp/image)

;; Image Image -> Boolean
;; Produces true if the area of img1 is greater than the area of img2.

(check-expect (first-large? (rectangle 30 10 "solid" "red") (rectangle 40 10 "solid" "blue")) false)
(check-expect (first-large? (rectangle 30 10 "solid" "red") (rectangle 30 10 "solid" "blue")) false)
(check-expect (first-large? (rectangle 50 10 "solid" "red") (rectangle 40 10 "solid" "blue")) true)
(check-expect (first-large? (rectangle 10 10 "solid" "red") (rectangle 40 10 "solid" "blue")) false)

;; (define (first-large? img1 img2) false)   ;stub

;; (define (first-large? img1 img2)           ;template
;; (... img1 img2))

(define (first-large? img1 img2)
  (> (* (image-width img1) (image-height img1))
       (* (image-width img2) (image-height img2))))
