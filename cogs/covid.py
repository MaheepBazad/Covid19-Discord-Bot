from multiprocessing.sharedctypes import Value
import discord
import requests
from discord.ext import commands
from quickchart import QuickChart


class covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, *, countryName=None):
        try:
            if countryName is None:
                await ctx.send("Add country's name to the command!")

            else:
                url = (
                    f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                )
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                totalDeaths = json_stats["deaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                todayCases = json_stats["todayCases"]
                todayDeaths = json_stats["todayDeaths"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
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
                                "label": "Graph on COVID19 Data",
                                "data": f"{todayCases},{totalDeaths},{recovered}",
                            }
                        ],
                    },
                }
                image = qc.get_url()
                embed = discord.Embed(
                    title=f"COVID19 data for {country}!",
                    description=f"These are the current stastics of the spread of coronavirus for {country}",
                    colour=0xF1C40F,
                    timestamp=ctx.message.created_at,
                )
                embed.add_field(name="Total Cases", value=totalCases, inline=True)
                embed.add_field(name="Total Deaths", value=totalDeaths, inline=True)
                embed.add_field(name="Recovered", value=recovered, inline=True)
                embed.add_field(name="Active Cases", value=active, inline=True)
                embed.add_field(name="Critical Cases", value=critical, inline=True)
                embed.add_field(name="Today's Cases", value=todayCases, inline=True)
                embed.add_field(name="Today's Deaths", value=todayDeaths, inline=True)
                embed.add_field(
                    name="Cases per million", value=casesPerOneMillion, inline=True
                )
                embed.add_field(
                    name="Deaths per million", value=deathsPerOneMillion, inline=True
                )
                embed.set_image(url=f"{image}")
                embed.set_thumbnail(
                    url="https://assets.weforum.org/article/image/Gt3_maI3Pg1p3LCdz686W_z41IEvOy6elJNQmu_oRLc.jpg"
                )
                await ctx.send(embed=embed)

        except:
            embed = discord.Embed(
                title="Invalid Country Name",
                colour=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            embed.set_author(name="Error!")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(covid(bot))
