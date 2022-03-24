import asyncio
from dotenv import load_dotenv

from Utils import logger


rootLogger = logger.getLogger()


async def runBotProcess(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()

    print(f'[{cmd!r} exited with {process.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


async def spawn_bots():
    rootLogger.info("Starting bots")
    await asyncio.gather(runBotProcess("ukraineGeneralGroupBot"), runBotProcess("ukraineHostRegistratorBot"))


def main():
    load_dotenv()

    # setup global logger
    logger.setupLogger()
    # logger
    asyncio.run(spawn_bots())
