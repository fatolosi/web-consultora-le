[Index.html](https://github.com/user-attachments/files/29777311/Index.html)
<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultora de Eficiencia Energética LE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        .gradient-text {
            background: linear-gradient(to right, #ef4444, #eab308, #22c55e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .gradient-bg {
            background: linear-gradient(135deg, #ef4444, #eab308, #22c55e);
        }
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-900">

    <!-- NAVEGACIÓN -->
    <nav class="fixed w-full z-50 bg-white/80 backdrop-blur-md border-b border-slate-100 py-4">
        <div class="container mx-auto px-6 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <!-- LOGO SIMBOLIZADO -->
                <div class="w-10 h-10 gradient-bg rounded-lg flex items-center justify-center text-white font-bold text-xl shadow-lg">
                    LE
                </div>
                <span class="font-extrabold text-xl tracking-tight">Consultora LE</span>
            </div>
            
            <div class="hidden md:flex items-center gap-8 font-semibold text-slate-600">
                <a href="#inicio" class="hover:text-green-600 transition-colors">Inicio</a>
                <a href="#servicios" class="hover:text-green-600 transition-colors">Servicios</a>
                <a href="#contacto" class="bg-green-600 text-white px-6 py-2 rounded-full hover:bg-green-700 transition-all shadow-md shadow-green-100">
                    Contacto
                </a>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section id="inicio" class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
        <div class="absolute top-0 left-0 w-full h-full -z-10 opacity-5">
            <div class="absolute top-[-10%] right-[-10%] w-[500px] h-[500px] bg-green-400 rounded-full blur-[120px]"></div>
            <div class="absolute bottom-[-10%] left-[-10%] w-[500px] h-[500px] bg-red-400 rounded-full blur-[120px]"></div>
        </div>

        <div class="container mx-auto px-6">
            <div class="flex flex-col lg:flex-row items-center gap-12 text-center lg:text-left">
                <div class="lg:w-1/2 space-y-8">
                    <div class="inline-block px-4 py-1.5 rounded-full bg-green-100 text-green-700 text-sm font-bold border border-green-200">
                        Sostenibilidad Real e Innovación
                    </div>
                    <h1 class="text-5xl lg:text-7xl font-extrabold leading-tight">
                        Eficiencia <span class="gradient-text">Energética</span> de Alto Nivel.
                    </h1>
                    <p class="text-xl text-slate-600 max-w-xl mx-auto lg:mx-0">
                        Transformamos el consumo de su empresa u hogar con soluciones tecnológicas avanzadas, auditorías precisas y energías renovables.
                    </p>
                    <div class="flex flex-wrap justify-center lg:justify-start gap-4">
                        <a href="#servicios" class="bg-slate-900 text-white px-8 py-4 rounded-2xl font-bold hover:bg-slate-800 transition-all shadow-xl">
                            Nuestras Soluciones
                        </a>
                        <a href="#contacto" class="bg-white border-2 border-slate-200 px-8 py-4 rounded-2xl font-bold hover:border-green-500 hover:text-green-600 transition-all">
                            Solicitar Asesoría
                        </a>
                    </div>
                </div>
                <div class="lg:w-1/2">
                    <div class="rounded-3xl overflow-hidden shadow-2xl border-[12px] border-white relative">
                        <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&q=80&w=1000" alt="Eficiencia Energética" class="w-full h-auto">
                        <div class="absolute bottom-4 left-4 bg-white/90 backdrop-blur p-4 rounded-xl shadow-lg border border-slate-100 hidden md:block">
                            <p class="text-xs font-bold text-slate-500 uppercase">Impacto Directo</p>
                            <p class="text-lg font-bold text-green-600">Ahorro Garantizado</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SERVICIOS -->
    <section id="servicios" class="py-24 bg-white">
        <div class="container mx-auto px-6">
            <div class="text-center max-w-3xl mx-auto mb-20 space-y-4">
                <h2 class="text-4xl font-extrabold">Nuestras Líneas de Negocio</h2>
                <div class="h-1.5 w-24 gradient-bg mx-auto rounded-full"></div>
                <p class="text-slate-500 text-lg pt-4">Soluciones integrales diseñadas para optimizar el rendimiento energético en cualquier sector.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- LOS 14 PUNTOS (Se eliminó el #11 de financiamiento automáticamente) -->
                
                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-green-600 mb-6 shadow-sm"><i data-lucide="bar-chart-3"></i></div>
                    <h3 class="text-xl font-bold mb-3">Auditorías Energéticas</h3>
                    <p class="text-slate-500 text-sm">Diagnóstico y análisis del consumo energético para identificar oportunidades de ahorro y soluciones personalizadas.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-yellow-500 mb-6 shadow-sm"><i data-lucide="sun"></i></div>
                    <h3 class="text-xl font-bold mb-3">Energía Renovable</h3>
                    <p class="text-slate-500 text-sm">Diseño e instalación de paneles solares fotovoltaicos, energía eólica a pequeña escala y calentadores solares.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-blue-500 mb-6 shadow-sm"><i data-lucide="activity"></i></div>
                    <h3 class="text-xl font-bold mb-3">Monitorización Real-Time</h3>
                    <p class="text-slate-500 text-sm">Implementación de software y hardware para optimizar el uso de energía mediante telemetría y análisis de datos.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-yellow-400 mb-6 shadow-sm"><i data-lucide="lightbulb"></i></div>
                    <h3 class="text-xl font-bold mb-3">Iluminación Inteligente</h3>
                    <p class="text-slate-500 text-sm">Sistemas LED de bajo consumo con sensores de movimiento y control automático para espacios públicos y privados.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-red-400 mb-6 shadow-sm"><i data-lucide="thermometer"></i></div>
                    <h3 class="text-xl font-bold mb-3">Optimización HVAC</h3>
                    <p class="text-slate-500 text-sm">Mejora de eficiencia en sistemas de climatización e instalación de equipos de alta eficiencia energética.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-slate-600 mb-6 shadow-sm"><i data-lucide="layers"></i></div>
                    <h3 class="text-xl font-bold mb-3">Aislamiento Térmico</h3>
                    <p class="text-slate-500 text-sm">Implementación de soluciones de aislamiento en edificios para reducir el consumo en calefacción y refrigeración.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-blue-600 mb-6 shadow-sm"><i data-lucide="car"></i></div>
                    <h3 class="text-xl font-bold mb-3">Movilidad Eléctrica</h3>
                    <p class="text-slate-500 text-sm">Instalación de puntos de carga y asesoría en la transición hacia flotas de vehículos eléctricos sostenibles.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-purple-600 mb-6 shadow-sm"><i data-lucide="graduation-cap"></i></div>
                    <h3 class="text-xl font-bold mb-3">Capacitación y Consultoría</h3>
                    <p class="text-slate-500 text-sm">Cursos especializados y asesoría en normativas ISO 50001, certificaciones LEED y BREEAM.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-orange-500 mb-6 shadow-sm"><i data-lucide="shopping-bag"></i></div>
                    <h3 class="text-xl font-bold mb-3">Venta de Tecnología</h3>
                    <p class="text-slate-500 text-sm">Distribución de electrodomésticos clase A+++ y dispositivos de domótica como termostatos inteligentes.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-emerald-600 mb-6 shadow-sm"><i data-lucide="users"></i></div>
                    <h3 class="text-xl font-bold mb-3">Comunidades Energéticas</h3>
                    <p class="text-slate-500 text-sm">Desarrollo de proyectos de autoconsumo compartido en comunidades de vecinos o polígonos industriales.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-green-700 mb-6 shadow-sm"><i data-lucide="leaf"></i></div>
                    <h3 class="text-xl font-bold mb-3">Huella de Carbono</h3>
                    <p class="text-slate-500 text-sm">Cálculo y reducción de emisiones con estrategias de compensación y obtención de certificados ambientales.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-cyan-600 mb-6 shadow-sm"><i data-lucide="building-2"></i></div>
                    <h3 class="text-xl font-bold mb-3">Sectores Específicos</h3>
                    <p class="text-slate-500 text-sm">Soluciones personalizadas para hotelería, retail, industria, agricultura e infraestructuras urbanas.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-indigo-600 mb-6 shadow-sm"><i data-lucide="cpu"></i></div>
                    <h3 class="text-xl font-bold mb-3">Innovación e IA</h3>
                    <p class="text-slate-500 text-sm">Implementación de Inteligencia Artificial y Machine Learning para optimizar el consumo de forma inteligente.</p>
                </div>

                <div class="service-card p-8 rounded-3xl bg-slate-50 border border-slate-100 transition-all duration-300">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-slate-800 mb-6 shadow-sm"><i data-lucide="wrench"></i></div>
                    <h3 class="text-xl font-bold mb-3">Mantenimiento y Soporte</h3>
                    <p class="text-slate-500 text-sm">Servicios preventivos y correctivos para asegurar que sus instalaciones operen siempre al 100% de su capacidad.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CONTACTO -->
    <section id="contacto" class="py-24 bg-slate-50">
        <div class="container mx-auto px-6">
            <div class="bg-white rounded-[3rem] shadow-2xl overflow-hidden flex flex-col lg:flex-row border border-slate-100">
                <!-- Info de contacto (MODIFICAR AQUÍ) -->
                <div class="lg:w-1/3 bg-slate-900 p-12 text-white">
                    <h2 class="text-3xl font-bold mb-8">Información de Contacto</h2>
                    <div class="space-y-8">
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 rounded-xl bg-white/10 flex items-center justify-center text-green-400"><i data-lucide="mail"></i></div>
                            <div>
                                <p class="text-xs text-slate-400 uppercase font-bold">Escríbanos</p>
                                <p class="font-medium">contacto@consultora-le.com</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 rounded-xl bg-white/10 flex items-center justify-center text-green-400"><i data-lucide="phone"></i></div>
                            <div>
                                <p class="text-xs text-slate-400 uppercase font-bold">Llámenos</p>
                                <p class="font-medium">+34 900 123 456</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 rounded-xl bg-white/10 flex items-center justify-center text-green-400"><i data-lucide="map-pin"></i></div>
                            <div>
                                <p class="text-xs text-slate-400 uppercase font-bold">Visítenos</p>
                                <p class="font-medium">Sede Central de Innovación, Ciudad</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Formulario -->
                <div class="lg:w-2/3 p-12">
                    <form action="#" class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-2">
                            <label class="text-sm font-bold text-slate-700">Nombre</label>
                            <input type="text" placeholder="Su nombre" class="w-full p-4 rounded-xl border border-slate-200 focus:ring-2 focus:ring-green-500 focus:outline-none">
                        </div>
                        <div class="space-y-2">
                            <label class="text-sm font-bold text-slate-700">Email</label>
                            <input type="email" placeholder="su@email.com" class="w-full p-4 rounded-xl border border-slate-200 focus:ring-2 focus:ring-green-500 focus:outline-none">
                        </div>
                        <div class="space-y-2 md:col-span-2">
                            <label class="text-sm font-bold text-slate-700">Mensaje</label>
                            <textarea rows="4" placeholder="¿En qué podemos ayudarle?" class="w-full p-4 rounded-xl border border-slate-200 focus:ring-2 focus:ring-green-500 focus:outline-none"></textarea>
                        </div>
                        <button type="submit" class="md:col-span-2 bg-green-600 text-white font-bold py-4 rounded-xl hover:bg-green-700 transition-all shadow-lg shadow-green-200">
                            Enviar Solicitud
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-white py-12 border-t border-slate-100">
        <div class="container mx-auto px-6 text-center space-y-6">
            <div class="flex justify-center items-center gap-2">
                <div class="w-8 h-8 gradient-bg rounded-lg flex items-center justify-center text-white font-bold text-sm">LE</div>
                <span class="font-bold text-slate-800 text-lg">Consultora LE</span>
            </div>
            <p class="text-slate-400 text-sm max-w-md mx-auto italic">"Liderando la transición energética hacia un futuro más limpio y rentable."</p>
            <div class="pt-6 border-t border-slate-50 text-slate-400 text-xs">
                © <span id="year"></span> Consultora de Eficiencia Energética LE. Todos los derechos reservados.
            </div>
        </div>
    </footer>

    <script>
        // Inicializar iconos
        lucide.createIcons();
        // Año automático en el footer
        document.getElementById('year').textContent = new Date().getFullYear();
    </script>
</body>
</html>
