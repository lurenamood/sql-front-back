1. Crear el proyecto de Reactjs con Nextjs:
   - Terminal CMD
   Comprobar que estas en la carpeta correcta comandos;
   dir --> ver todas las carpetas 
   cd nombre-de-la-carpeta --> para entrar en la carpeta

   Comando para crear con Nextjs
   npx create-next-app@latest nombre-del-proyecto

   Te preguntara a continuación AQUI LA CONFIG. MIA
  	What is your project named?  nombre-de-la-app
	1. Would you like to use TypeScript?  No / Yes [ELEGIR SI TS o JS]
	2. Would you like to use ESLint?   Yes
	3. Would you like to use Tailwind CSS? Yes [Si no vas a usarlo no]
	4. Would you like your code inside a `src/` directory?  Yes
	5. Would you like to use App Router? (recommended)  Yes
	6. Would you like to use Turbopack for `next dev`? Yes
	7. Would you like to customize the import alias (`@/*` by default)?  No / Yes

		a. Poner uno solo en la terminal (@/*)
			// Presionar Enter para darle al OK

		b. Luego editar jsconfig.json para agregar los demás alias
			EJ. de alias --> Es un Obj ACUERDATE de las comas
			"@utils/*": ["./src/utils/*"],
			"@hooks/*": ["./src/hooks/*"],
			"@styles/*": ["./src/styles/*"],
			"@assets/*": ["./src/assets/*"],

			ASÍ QUEDARIA 
			import Header from '@components/ui/Header';

		Aqui es para crear atajos cuando importas algo en vez de usar


2. Ejecutar en terminal para comprobar si funciona:
		-	npm run dev

3. Comprobar si estas en la carpeta del proyecto FRONT-END comandos:
		cd..  [ para ir hacia atras en una carpeta por la terminal en CMD ]
		Entrar en la carpeta del Front 
		-   npm install axios   --> para poder hacer las peticiones con Endpoints al back

4. En las peticiones con Axios a la /api del BACK comprueba:
		naming de las rutas ej:  "@services/": ["./src/services/*"]
		naming de la VARIABLES
		naming DATABASE
		naming las columnas de la DATABASE ( ej: US_nombre, US_apellido . . .)


5. ARQUITECTURA RECOMENDADA:
frontend/
├── app/                    # App Router (v13+)
│   ├── layout.js           # Layout general
│   ├── page.js             # Home
│   └── dashboard/          # Ruta protegida
├── components/             # Componentes UI compartidos
├── hooks/                  # Custom React hooks
├── lib/                   # Firebase, axios, helpers
├── services/              # Lógica externa, API calls
├── store/                 # Zustand state management
├── styles/                # Tailwind + Global CSS
├── utils/                 # Validadores, formatters, etc
└── public/                # Imágenes y assets


----------------------------------------------------------------------------------------------------------------------
RESUMEN DE COMANDOS: 
cd nombre-de-la-carpeta [ para entrar en la carpeta ]
cd..  [ para ir hacia atras en una carpeta por la terminal en CMD ]
-	npm run dev  --> ver el proyecto en la web
-   npm install axios ---> libreria de Reactjs para  poder hacer peticiones al back