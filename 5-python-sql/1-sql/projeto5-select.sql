-- 1. Quem dá aulas de Geometria Analítica?

SELECT p.nm_professor, d.nm_disciplina
FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
WHERE UPPER(d.nm_disciplina) LIKE '%GEOMETRIA ANALITICA%';

-- 2. Onde os professores de Geometria Analítica moram?

SELECT p.nm_professor, d.nm_disciplina, b.nm_bairro FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
INNER JOIN bairros b ON b.id_bairro = p.id_bairro
WHERE UPPER(d.nm_disciplina) LIKE '%GEOMETRIA ANALITICA%';

-- 3. Quem dá Laboratório de Cálculo à tarde?

SELECT p.nm_professor, d.nm_disciplina, t.turno
FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
WHERE t.turno = 'tarde'
AND d.nm_disciplina = 'Laboratorio de Calculo';

-- 4. Quem dá Laboratório de Cálculo ou Computação à tarde?

SELECT p.nm_professor, d.nm_disciplina, t.turno
FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
WHERE t.turno = 'tarde'
AND d.nm_disciplina IN ('Laboratorio de Calculo', 'Laboratorio de Computacao');

SELECT p.nm_professor, d.nm_disciplina, t.turno
FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
WHERE (d.nm_disciplina = 'Laboratorio de Calculo' 
OR d.nm_disciplina = 'Laboratorio de Computacao')
AND t.turno = 'tarde';

-- Vai dar a resposta errada:
SELECT p.nm_professor, d.nm_disciplina, t.turno
FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
WHERE d.nm_disciplina = 'Laboratorio de Calculo' 
OR (d.nm_disciplina = 'Laboratorio de Computacao'
AND t.turno = 'tarde');


select * from turmas where id_disciplina in(8, 9) order by id_disciplina;

-- 5. Quem dá Laboratório (de qualquer matéria) à tarde?

SELECT p.nm_professor, d.nm_disciplina, t.turno FROM turmas t
INNER JOIN professores p ON p.id_professor = t.id_professor
INNER JOIN disciplinas d ON d.id_disciplina = t.id_disciplina
WHERE d.nm_disciplina LIKE '%Laboratorio%'
AND t.turno = 'tarde';

-- 6. Quais são os professores têm mais de 32 anos?

CREATE TABLE professores (
    id_professor SERIAL PRIMARY KEY, 
    nm_professor VARCHAR NOT NULL, 
    data_nascimento TIMESTAMP NOT NULL, 
    id_bairro INTEGER NOT NULL REFERENCES bairros
);

INSERT INTO professores (nm_professor, data_nascimento, id_bairro)
VALUES ('Vitinho', '1993-12-24', 1);

SELECT 
    nm_professor, 
    NOW()::date, 
    data_nascimento, 
    DATE_PART('year', NOW()), 
    DATE_PART('year', data_nascimento),
    DATE_PART('year', NOW()) - DATE_PART('year', data_nascimento) idade
  from professores
  where DATE_PART('year', NOW()) - DATE_PART('year', data_nascimento) > 32;


SELECT * FROM
(
SELECT 
    nm_professor, 
    DATE_PART('year', NOW()) - DATE_PART('year', data_nascimento) idade
  from professores
) temp
WHERE idade > 32;
  
