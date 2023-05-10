import asyncio
async def mostrar_mensaje(tiempo, texto):
    await asyncio.sleep(tiempo)
    print(texto)

async def main():
    tarea1 = asyncio.create_task(mostrar_mensaje(5, 'primero ejecuto yo'))
    tarea2 = asyncio.create_task(mostrar_mensaje(10, 'segundo yo'))
    tarea3 = asyncio.create_task(mostrar_mensaje(0, 'último'))

    await tarea1
    await tarea2
    await tarea3

asyncio.run(main())