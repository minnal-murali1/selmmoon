from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start8{CMD_INDEX}'
        self.MirrorCommand = f'mirror8{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror8{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirror8{CMD_INDEX}'
        self.CancelMirror = f'cancel8{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall8{CMD_INDEX}'
        self.ListCommand = f'list8{CMD_INDEX}'
        self.SearchCommand = f'search8{CMD_INDEX}'
        self.StatusCommand = f'status8{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users8{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize8{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize8{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo8{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo8{CMD_INDEX}'
        self.PingCommand = f'ping8{CMD_INDEX}'
        self.RestartCommand = f'restart8{CMD_INDEX}'
        self.StatsCommand = f'stats8{CMD_INDEX}'
        self.HelpCommand = f'help8{CMD_INDEX}'
        self.LogCommand = f'log8{CMD_INDEX}'
        self.CloneCommand = f'clone8{CMD_INDEX}'
        self.CountCommand = f'count8{CMD_INDEX}'
        self.WatchCommand = f'watch8{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch8{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirror8{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirror8{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirror8{CMD_INDEX}'
        self.DeleteCommand = f'del8{CMD_INDEX}'
        self.ShellCommand = f'shell8{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp8{CMD_INDEX}'
        self.LeechSetCommand = f'leechset8{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb8{CMD_INDEX}'
        self.SpeedCommand = f'speedtest8{CMD_INDEX}'
        self.LeechCommand = f'leech8{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech8{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech8{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech8{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech8{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech8{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch8{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch8{CMD_INDEX}'
        self.RssListCommand = f'rsslist8{CMD_INDEX}'
        self.RssGetCommand = f'rssget8{CMD_INDEX}'
        self.RssSubCommand = f'rsssub8{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub8{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset8{CMD_INDEX}'

BotCommands = _BotCommands()
