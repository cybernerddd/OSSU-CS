; Design a function called square that
; 
; consumes a Number and produces its square.


;;Number -> Number
;; multiplies the given number by itself(square)

(check-expect (square 5) (* 5 5))
(check-expect (square 4) 16)

;;(define (square n) 0)  ; stub

;;(define (square n)   ;template
 ;; (... n))

(define (square n)
  (* n n))
