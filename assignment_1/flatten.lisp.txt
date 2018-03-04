(defun flatten (l) (if( not (eq (car (cdr (cdr l))) nil)) l (flatten (append (car l) (car (reverse l))))))
