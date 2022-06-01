import discord
import requests
from discord.ext import commands


class india(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="india")
    async def india(self, ctx, *, state=None):
        try:
            if state is None:
                await ctx.send("Add state's name to the command!")

            else:
                url = "https://covid-19-india2.p.rapidapi.com/details.php"

                headers = {
                    "X-RapidAPI-Host": "covid-19-india2.p.rapidapi.com",
                    "X-RapidAPI-Key": "07e8df961bmsh592a2dd1213373fp11a2e7jsn369e6d4970ea",
                }
                data = requests.get(url, headers=headers).json()
                for state in data:
                    state = data["state"]
                    totalCases = data["total"]
                    totalDeaths = data["death"]
                    recovered = data["cured"]
                    embed = discord.Embed(
                        title=f"COVID19 data for {state}!",
                        description=f"These are the current stastics of the spread of coronavirus for {state}",
                        colour=0xF1C40F,
                        timestamp=ctx.message.created_at,
                    )
                    embed.add_field(name="Place", value=state, inline=True)
                    embed.add_field(name="Total Cases", value=totalCases, inline=True)
                    embed.add_field(name="Deaths", value=totalDeaths, inline=True)
                    embed.add_field(name="Recovered", value=recovered, inline=True)

                    embed.set_thumbnail(
                        url="https://assets.weforum.org/article/image/Gt3_maI3Pg1p3LCdz686W_z41IEvOy6elJNQmu_oRLc.jpg"
                    )
                    await ctx.send(embed=embed)

        except:
            await ctx.send("Incorrect State Name!!")


def setup(bot):
    bot.add_cog(india(bot))
