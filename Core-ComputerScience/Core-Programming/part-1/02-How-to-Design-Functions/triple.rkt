; Design a function called triple that consumes
; a Number and produces three times that number.
; 


;; Number -> Number
;; produces three times the supplied number

(check-expect (triple 2) 6)
(check-expect (triple 3) 9)

;; (define (triple n) 0)   ;stub

;;(define (triple n)       ;template
;; (... n))

(define (triple n)
  (* 3 n))
