-- Please write a DELETE statement and DO NOT write a SELECT statement.

DELETE P1 FROM Person as P1, Person as P2
WHERE P1.id > P2.id AND P1.email = P2.email;