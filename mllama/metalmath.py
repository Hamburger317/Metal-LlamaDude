import math
import discord

math_commands = discord.SlashCommandGroup("math", "Standard math utils.")
math_operators = math_commands.create_subgroup("operator", "Operators")


@math_operators.command(description="Add x with y.")
async def add(ctx, x: int, y: int):
    await ctx.respond(x + y)


@math_operators.command(description="Subtract x with y.")
async def sub(ctx, x: int, y: int):
    await ctx.respond(x - y)


@math_operators.command(description="Multiply x by y.")
async def multiply(ctx, x: int, y: int):
    await ctx.respond(x * y)


@math_operators.command(description="Divide x by y.")
async def divide(ctx, x: int, y: int):
    if not y:
        await ctx.respond("You can't divide by 0, silly.")

        return

    await ctx.respond(x / y)


@math_operators.command(description="Get the remainer of the divison.")
async def mod(ctx, x: int, y: int):
    if not y:
        await ctx.respond("You can't divide by 0, silly.")
        return

    await ctx.respond(x % y)


@math_operators.command(description="Raise x to y power.")
async def pow(ctx, x: int, y: int):
    await ctx.respond(x**y)


math_trig = math_commands.create_subgroup("trig", "Trigonometric functions")


@math_trig.command(description="Calculate sine of x in radians")
async def sin(ctx, x: int):
    await ctx.respond(math.sin(x))


@math_trig.command(description="Calculate cos of x in radians")
async def cos(ctx, x: int):
    await ctx.respond(math.cos(x))


@math_trig.command(description="Calculate tan of x in radians")
async def tan(ctx, x: int):
    await ctx.respond(math.tan(x))


math_other = math_commands.create_subgroup("other", "Other misc math functions")


@math_other.command(description="Calculate square root of X.")

async def squareroot(ctx, x: int):
    try:
        answer = math.sqrt(x)

    except ValueError:
        await ctx.respond("Domain error")
        return

    await ctx.respond(answer)


@math_other.command(description="Calculate cube root of x")
async def cuberoot(ctx, x: int):
    try:
        answer = math.cbrt(x)

    except ValueError:
        await ctx.respond("Domain error")
        return

    await ctx.respond(answer)
