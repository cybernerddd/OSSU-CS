; Design a function called fahrenheit-to-celsius
; that consumes a temperature in Fahrenheit
; and produces the equivalent temperature in Celsius.
; 


;;Number -> Number
;;subtracts 32 from n and divide by 1.8(formula)

(check-expect (fahrenheit-to-celsius 212) 100)
(check-expect (fahrenheit-to-celsius 98.6) 37)

;;(define (fahrenheit-to-celsius n) 0)    ;stub

;(define (fahrenheit-to-celsius n)    ;template
 ; (...n))

(define (fahrenheit-to-celsius n)
  (/ (- n 32) 1.8))
