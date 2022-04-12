Select count(Id) as "Count"
from Ciudadanos_Actividades AS t WITH (NOLOCK)
where (t.pilar360Id IS NOT NULL) AND (CONVERT(DATE, CONVERT(VARCHAR(10), t.CreatedDate, 101), 101)  = '2022/04/11' ) 