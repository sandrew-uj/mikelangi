from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

conf_callback = CallbackData("confirm", "action")

confirmation_keyboard = InlineKeyboardMarkup(
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Оставить",
                                          callback_data=conf_callback.new(action="save")
                                      ),
                                  ]
                              ])
