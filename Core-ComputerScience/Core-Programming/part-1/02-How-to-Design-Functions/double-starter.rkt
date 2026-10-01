
;; double-starter.rkt

; 
; PROBLEM:
; 
; Design a function that consumes a number and produces twice that number. 
; Call your function double. Follow the HtDF recipe and leave behind commented 
; out versions of the stub and template.
; 



;; Number -> Number

;; double the given number

; (define (double n) 0)

(check-expect (double 3) (* 2 3))
(check-expect (double 4.2) 8.4)

;(define (double n)
;  (... n))

(define (double n)
  (* 2 n))
