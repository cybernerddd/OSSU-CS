
;; less-than-five-starter.rkt

; 
; PROBLEM:
; 
; DESIGN function that consumes a string and determines whether its length is
; less than 5.  Follow the HtDF recipe and leave behind commented out versions 
; of the stub and template.
; 


;; String -> Boolean
;; Produce true if the length of the given string is less than 5

(check-expect (less-than-five? "school") false)
(check-expect (less-than-five? "") true)
(check-expect (less-than-five? "scl") true)
(check-expect (less-than-five? "small") false)

;(define (less-than-five? s) false)       ;stub

;(define (less-than-five? s)              ;template
 ; (... s))

(define (less-than-five? s)
  (< (string-length s) 5))

