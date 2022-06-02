import discord
import requests
from discord.ext import commands
from quickchart import QuickChart

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
                state = data[f'{state}']["state"]
                totalCases = data[f'{state}']["total"]
                totalDeaths = data[f'{state}']["death"]
                recovered = data[f'{state}']["cured"]
                qc = QuickChart()
                qc.width = 500
                qc.height = 300
                qc.device_pixel_ratio = 2
                qc.config = {
                    "type": "bar",
                    "data": {
                        "labels": ["Total cases", "Deaths", "Recovered"],
                        "datasets": [
                            {
                                "label": "Graph on COVID19 Data ",
                                "data": [totalCases, totalDeaths, recovered],
                            }
                        ],
                    },
                }
                image = qc.get_url()
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
                embed.set_image(url=f"{image}")
                embed.set_thumbnail(
                    url="https://gumlet.assettype.com/greaterkashmir%2F2022-05%2Ffb121dec-0760-495b-93f2-ddcab7f8c400%2F2402f44620132cab0e9832b0fe454228.jpg?format=auto"
                )
                await ctx.send(embed=embed)

        except:
            await ctx.send("Incorrect State Name!!")


def setup(bot):
    bot.add_cog(india(bot))


