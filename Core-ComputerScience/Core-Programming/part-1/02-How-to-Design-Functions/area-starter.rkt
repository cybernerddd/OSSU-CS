
;; area-starter.rkt

; 
; PROBLEM:
; 
; DESIGN a function called area that consumes the length of one side 
; of a square and produces the area of the square.
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


;; Number -> Number
;; given the length of one side of the square, produce the area of the square

(check-expect (area 5) 25)
(check-expect (area 7) 49)

; (define (area s) 0)   ;STUB

;(define (area s)   ;template
 ; (... s))

(define (area s)
  (* s s))
