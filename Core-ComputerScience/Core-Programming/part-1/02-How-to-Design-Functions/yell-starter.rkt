
;; yell-starter.rkt

; 
; PROBLEM:
; 
; DESIGN a function called yell that consumes strings like "hello" 
; and adds "!" to produce strings like "hello!".
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 



;; String -> String    ;signature
;;produce string with "!" added to the end of the given string   ;purpose

;;(define (yell word) "") ;stub

(check-expect (yell "size") "size!")           ;examples
(check-expect (yell "hello") "hello!")


;(define (yell word)     ;template
;  (... word))

(define (yell word)
  (string-append word "!"))
