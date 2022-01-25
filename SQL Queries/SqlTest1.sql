Select count(Id) as "Count"
from Ciudadanos_Actividades AS t WITH (NOLOCK)
where (t.pilar360Id IS NOT NULL) 