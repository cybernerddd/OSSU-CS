; Design a function called greet that consumes a String and produces:
; 
; "Hello, NAME!"


;; String -> String
;; adds "Hello," in front of the name to greet and appends "!" at the end.

(check-expect (greet "Cybernerddd") "Hello, Cybernerddd!")
(check-expect (greet "michael") "Hello, michael!")

;;(define (greet str) "")   ;stub

;(define (greet name)    ;template
;  (... name...))   

(define (greet name) 
  (string-append "Hello, " name "!"))
