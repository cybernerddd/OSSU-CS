; Design a function called cyber-score
; that consumes a Number representing the
; number of flags captured in a CTF and
; produces twice the number of flags.
; 


;; Number -> Number
;; produces two times the given number

(check-expect (cyber-score 5) 10)
(check-expect (cyber-score 6.2) 12.4)

;;(define (cyber-score n) 0)  ;stub

;;(define (cyber-score n)
;;  (...n))

(define (cyber-score n)
  (* 2 n))
