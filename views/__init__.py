from .animal_requests import get_all_animals
from .animal_requests import get_single_animal 
from .animal_requests import create_animal
from .animal_requests import update_animal
from .animal_requests import get_animals_by_location
from .animal_requests import get_animals_by_status
from .animal_requests import delete_animal

from .location_requests import get_all_locations
from .location_requests import get_single_location
from .location_requests import create_location
from .location_requests import delete_location
from .location_requests import update_location

from .employee_requests import get_single_employee
from .employee_requests import get_all_employees
from .employee_requests import create_employee
from .employee_requests import delete_employee
from .employee_requests import update_employee
from .employee_requests import get_employees_by_location

from .customer_requests import get_single_customer
from .customer_requests import get_all_customers
from .customer_requests import create_customer
from .customer_requests import delete_customer
from .customer_requests import update_customer
from .customer_requests import get_customers_by_email