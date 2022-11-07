from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'mirror2{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror2{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirro2{CMD_INDEX}'
        self.CancelMirror = f'cancel2{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall2{CMD_INDEX}'
        self.ListCommand = f'list2{CMD_INDEX}'
        self.SearchCommand = f'search2{CMD_INDEX}'
        self.StatusCommand = f'status2{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users2{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize2{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize2{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo2{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo2{CMD_INDEX}'
        self.PingCommand = f'ping2{CMD_INDEX}'
        self.RestartCommand = f'restart2{CMD_INDEX}'
        self.StatsCommand = f'stats2{CMD_INDEX}'
        self.HelpCommand = f'help2{CMD_INDEX}'
        self.LogCommand = f'log2{CMD_INDEX}'
        self.CloneCommand = f'clone2{CMD_INDEX}'
        self.CountCommand = f'count2{CMD_INDEX}'
        self.WatchCommand = f'watch2{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch2{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirror2{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirror2{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirror2{CMD_INDEX}'
        self.DeleteCommand = f'del2{CMD_INDEX}'
        self.ShellCommand = f'shell2{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp2{CMD_INDEX}'
        self.LeechSetCommand = f'leechset2{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb2{CMD_INDEX}'
        self.LeechCommand = f'leech2{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech2{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech2{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech2{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech2{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech2{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch2{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch2{CMD_INDEX}'
        self.BtSelectCommand = f'btsel2{CMD_INDEX}'
        self.RssListCommand = f'rsslist2{CMD_INDEX}'
        self.RssGetCommand = f'rssget2{CMD_INDEX}'
        self.RssSubCommand = f'rsssub2{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub2{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset2{CMD_INDEX}'
        self.EvalCommand = f'eval2{CMD_INDEX}'
        self.ExecCommand = f'exec2{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals2{CMD_INDEX}'
        self.SleepCommand = f'sleep2{CMD_INDEX}'

BotCommands = _BotCommands()
