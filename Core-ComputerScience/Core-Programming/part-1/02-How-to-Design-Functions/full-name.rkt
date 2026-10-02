; Design a function called full-name that consumes two Strings:
; 
; first name
; last name
; 
; and produces one string containing the full name separated by a space.


;; String String -> String
;; produces a string that appends first and last

(check-expect (full-name "Emmanuel" "Ampah") "Emmanuel Ampah")
(check-expect (full-name "max" "klemp") "max klemp")

;;(define (full-name first last) "")    ; stub

;;(define (full-name first last)    ;template
  ;;(... first last))

(define (full-name first last)
  (string-append first " " last))

