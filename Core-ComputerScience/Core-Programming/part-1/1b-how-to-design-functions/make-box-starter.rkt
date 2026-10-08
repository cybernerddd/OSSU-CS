(require 2htdp/image)

;; make-box-starter.rkt

; 
; PROBLEM:
; 
; You might want to create boxes of different colours.
; 
; Use the How to Design Functions (HtDF) recipe to design a function that consumes a color, and creates a 
; solid 10x10 square of that colour.  Follow the HtDF recipe and leave behind commented out versions of
; the stub and template.
; 


;; String -> Image
;; produces a 10x10 square of the given color

(check-expect (make-box "red") (square 10 "solid" "red"))
(check-expect (make-box "green") (square 10 "solid" "green"))

; (define (make-box c) (square 10 "solid" "white")) ;stub

;; (define (make-box c)                                ;template
;;   (... c)

(define (make-box c)
  (square 10 "solid" c ))
